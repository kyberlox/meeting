<template>
    <div class="relative w-full">
        <!-- Контейнер с изображением -->
        <div class="w-full h-auto bg-no-repeat bg-cover bg-center"
             :style="{ 'background-image': `url(${img})` }">
            <div class="sm:pb-[65.5%] md:pb-[40.5%] lg:pb-[32%] pb-[100%]"></div>
        </div>

        <!--  текст -->
        <div class="absolute inset-0 flex items-center">
            <div
                 class="text-left text-white p-3 sm:p-4 md:p-6 lg:p-8 text-md sm:text-xl md:text-3xl lg:text-5xl xl:text-6xl 2xl:text-7xl ml-2 sm:ml-4 md:ml-8 lg:ml-16 xl:ml-24 max-w-full">
                <span class="font-medium">21-22 АВГУСТА</span>
                <br />
                <span class="text-theme-orange text-theme-orange font-bold leading-[105%] sm:leading-[110%]">VII
                    МЕЖДУНАРОДНАЯ
                    <br />
                    ПРОЕКТНАЯ КОНФЕРЕНЦИЯ <br />
                    ПО ТРУБОПРОВОДНЫМ СИСТЕМАМ <br /></span>
                <span
                      class="font-light text-theme-white text-xs sm:text-sm md:text-xl lg:text-2xl xl:text-3xl block mt-1 sm:mt-2 md:mt-3">
                    Организатор АО «МОСЦКБА» при поддержке НПАА
                </span>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { page } from "@/assets/data";
export default defineComponent({
    name: 'DownHeaderPhoto',
    setup() {
        const img = page.firstImg;
        return {
            img
        }
    }
})
</script>