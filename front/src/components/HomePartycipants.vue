<template>
    <div class="partycipants-preview__wrapper p-2 sm:p-4 w-full max-w-7xl mt-6 sm:mt-8 md:mt-10 mx-auto">
        <div
             class="partycipants-preview__title text-xl sm:text-2xl md:text-3xl mt-6 sm:mt-8 md:mt-10 text-center font-bold text-theme-black mb-2 sm:mb-4">
            Участники
        </div>
        <div
             class="partycipants-preview mt-6 sm:mt-8 md:mt-10 grid  grid-cols-2 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-auto gap-2 sm:gap-3 md:gap-4">
            <div class="partycipants-preview__item flex justify-center items-center m-auto"
                 v-for="(item, index) in galleryItems"
                 :key="index + 'slide'">
                <div
                     class="partycipants-preview__item__image transition-transform duration-300 ease-in-out hover:scale-105">
                    <img class="rounded-xl w-full h-auto max-w-[120px] sm:max-w-[150px] md:max-w-[180px]"
                         :src="item"
                         alt="Participant logo" />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { page } from '@/assets/data';
export default defineComponent({
    name: 'PartycipantsBlock',
    setup() {
        return {
            galleryItems: page.partycipants
        }
    }
})
</script>