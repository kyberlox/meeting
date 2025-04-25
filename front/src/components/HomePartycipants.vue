<template>
    <div v-if="visibleLogos"
         class="partycipants-preview__wrapper p-2 sm:p-4 w-full max-w-7xl  mx-auto">
        <div
             class="partycipants-preview__title text-xl sm:text-2xl md:text-3xl  text-center font-bold text-theme-black mb-2 sm:mb-4">
            В наших мероприятиях приняли участие следующие клиенты:
        </div>
        <transition-group name="logo-list"
                          tag="div"
                          class="partycipants-preview mt-6 sm:mt-8 md:mt-10 grid  grid-cols-2 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-auto gap-2 sm:gap-3 md:gap-4">
            <div class="partycipants-preview__item flex justify-center items-center m-auto"
                 v-for="(item, index) in visibleLogos"
                 :key="index + 'slide'">
                <div
                     class="partycipants-preview__item__image transition-transform duration-300 ease-in-out hover:scale-105">
                    <img class="rounded-xl w-full h-auto max-w-[120px] sm:max-w-[150px] md:max-w-[180px]"
                         :src="item"
                         alt="Participant logo" />
                </div>
            </div>
        </transition-group>
        <div class="flex justify-center mt-6"
             v-if="!showAll">
            <button @click="showAll = true"
                    class="bg-theme-blue-dark hover:bg-[var(--theme-blue-light)]! cursor-pointer text-xl py-2 px-6 rounded-md transition-colors bg-theme-blue-dark text-white duration-300 shadow-sm hover:shadow-md">
                Показать все
            </button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, watch } from 'vue';
import { page } from '@/assets/data';
export default defineComponent({
    name: 'PartycipantsBlock',
    setup() {
        const logos = ref();
        const showAll = ref(false);
        const visibleLogos = ref();
        const API_URL = "https://meeting.mosckba.ru/api";
        onMounted(() => {
            fetch(API_URL + '/logos')
                .then(res => res.json())
                .then(data => {
                    logos.value = data;
                    visibleLogos.value = logos.value.slice(0, 12);
                })
                .catch(err => console.log(err))
        })

        watch(showAll, () => {
            if (showAll.value == false) {
                visibleLogos.value = logos.value.slice(0, 10);
            }
            else {
                visibleLogos.value = logos.value;
            }
        });
        return {
            logos,
            showAll,
            visibleLogos
        }
    }
})
</script>

<style scoped>
/* Анимация для появления логотипов */
.logo-list-enter-active,
.logo-list-leave-active {
    transition: all 0.5s ease;
}

.logo-list-enter-from {
    opacity: 0;
    transform: translateY(30px);
}

.logo-list-leave-to {
    opacity: 0;
}

/* Задержка для каскадного появления */
.logo-list-item {
    transition-delay: calc(var(--i, 0) * 0.05s);
}
</style>