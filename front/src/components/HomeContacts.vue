<template>
    <div class="printed-container pb-10 mt-20">
        <div
             class="contacts text-theme-blue-dark pt-10 font-semibold text-base sm:text-lg md:text-xl lg:text-2xl  max-w-xs sm:max-w-sm md:max-w-md m-auto text-center">
            По вопросам участия и любым другим вопросам свяжитесь с нами удобным способом:
        </div>
        <div class="flex flex-row max-w-7xl m-auto flex-wrap items-center justify-center gap-10 md:gap-20 p-10">
            <HomeForm />
            <div class="contacts__wrapper mb-auto">
                <div class="contacts py-6 sm:py-8 md:py-10">
                    <div
                         class="contacts__text text-theme-blue-dark break-normal font-medium flex flex-col justify-center gap-1 sm:gap-2 text-lg sm:text-xl md:text-2xl max-w-xs sm:max-w-sm md:max-w-md m-auto text-center mt-3 sm:mt-4 md:mt-5">
                        <span class="break-words"> {{ phone }}</span>
                        <span class="break-words"> {{ phoneInner }}</span>
                        <span class="mt-1 sm:mt-2 break-words"> {{ email }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { page } from '@/assets/data'
import HomeForm from './HomeForm.vue'
export default defineComponent({
    components: {
        HomeForm
    },
    setup() {
        return {
            phone: page.phone,
            email: page.email,
            phoneInner: page.phoneInner
        }
    }
})
</script>
