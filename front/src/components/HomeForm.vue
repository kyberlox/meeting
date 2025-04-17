<template>
    <div class="form-wrapper max-w-[450px] grow min-h-[max-content] bg-white p-6 rounded-lg shadow-md">
        <section class="form grid grid-cols-2 gap-x-[10px] space-y-4">
            <div class="form-input"
                 v-for="item in form"
                 :key="item.id"
                 :class="{ 'col-span-2': item.name == 'fio' || item.name == 'msg' || item.name == 'email' || item.name == 'report' }">
                <label class="block text-gray-700 text-md font-medium"
                       :class="{ 'mb-2': item.type !== 'checkbox', 'flex flex-row-reverse items-center gap-[6px] justify-end cursor-pointer': item.type == 'checkbox' }">{{
                        item.title }}
                    <input :type="item.type"
                           :placeholder="item.placeholder"
                           @input="setData(item.name, item.type !== 'checkbox' ? ($event.target as HTMLInputElement).value : ($event.target as HTMLInputElement).checked)"
                           class="mt-1"
                           :class="[
                            item.type === 'checkbox' ? 'h-5 w-5 text-blue-600' : 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-300 focus:border-blue-500',
                        ]" />
                </label>
                <div v-if="v$.formResults[item.name]?.$error"
                     class="text-red-500 text-sm">{{ v$.formResults[item.name].$errors[0].$message }}</div>

            </div>
        </section>
        <div class="">

            <button class="form-btn hover:bg-[var(--theme-blue-light)]! text-white min-w-[120px] relative min-h-[44px] mt-5 cursor-pointer  text-lg  py-2 px-4 rounded-md transition-colors bg-theme-blue-dark  duration-300 shadow-sm hover:shadow-md flex justify-center items-center"
                    :class="{ 'disabled': loading }">
                <span v-if="!loading"
                      @click="submitForm()">Отправить
                </span>
                <span v-else
                      class="loader">
                </span>
            </button>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, type Ref, computed, ref } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required, email, helpers } from '@vuelidate/validators';
import { useToast } from "vue-toastification";
import { page } from '@/assets/data';

// фио, телефон, организация, email, галочка с докладом
export default defineComponent({
    setup() {
        const form = page.formData;

        interface IForm {
            fio?: string;
            phone?: string;
            email?: string;
            organization?: string;
            report: boolean;
            msg?: string;
            [key: string]: string | boolean | undefined;
        };

        const loading = ref(false);

        const toast = useToast();

        const formResults: Ref<IForm> = ref({
            report: false,
        });

        const rules = computed(() => ({
            formResults: {
                fio: {
                    required: helpers.withMessage('ФИО обязательно для заполнения', required)
                },
                phone: {
                    required: helpers.withMessage('Телефон обязателен для заполнения', required),
                    phoneFormat: helpers.withMessage('Введите корректный номер телефона', helpers.regex(/^(\+7|8)[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$/))
                },
                email: {
                    required: helpers.withMessage('Email обязателен для заполнения', required),
                    email: helpers.withMessage('Введите корректный email', email)
                },
                organization: {
                    // required: helpers.withMessage('Организация обязательна для заполнения', required)
                },
                msg: {
                    // 
                }
            }
        }));

        const v$ = useVuelidate(rules, { formResults });

        const setData = (name: string, value: string | boolean) => {
            formResults.value[name] = value;
            v$.value.formResults[name].$touch();
        };

        const submitForm = async () => {
            const isFormCorrect = await v$.value.$validate();
            if (!isFormCorrect) {
                return;
            }
            else {
                loading.value = true;
                sendEmail();
            }
        };

        const sendEmail = () => {
            fetch('http://meeting.mosckba.ru:8000/api/send_form', {
                method: 'POST',
                body: JSON.stringify(formResults.value),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(response => response.json())
                .then(data => {
                    if (data == true) {
                        toast.success('Сообщение успещно отправлено!')
                    };
                    loading.value = false;
                })
                .catch(error => {
                    toast.error('Что-то пошло не так, повторите попытку позже');
                    console.error('Error submitting form:', error);
                    loading.value = false;
                });
        }

        return {
            form,
            submitForm,
            setData,
            v$,
            loading
        }
    }
})


</script>