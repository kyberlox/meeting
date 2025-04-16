<template>
    <div class="printed-container">
        <div class="gallery-preview__wrapper  mb-10 p-2 max-w-7xl printed-container mx-auto">
            <!-- <div class="gallery-preview__title text-2xl mt-10 text-center font-bold text-theme-black mb-4">{{
                galleryTitle
            }}</div> -->
            <div class="gallery-preview mt-10 grid grid-cols-3 gap-4">
                <div class="gallery-preview__item"
                     v-for="(item, index) in galleryItems"
                     :key="index + 'slide'">
                    <div class="gallery-preview__item__image">
                        <img class="rounded-xl"
                             :src="item" />
                    </div>
                </div>
            </div>
            <div class="gallery-preview__button text-center -mt-5">
                <button @click="goToGallery"
                        class="btn-primary bg-theme-blue-dark text-black font-medium py-2 px-4 rounded-md transition-colors
                    duration-300 text-xl shadow-sm hover:shadow-md">Посмотреть
                    все</button>

            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { page } from '@/assets/data'
import { useRouter } from 'vue-router'
export default defineComponent({

    setup() {
        const router = useRouter();
        const goToGallery = () => {
            router.push('/archive/2024').then(() => {
                window.scrollTo(0, 0);
            });
        }
        return {
            // galleryTitle: page.galleryPreviewTitle,
            galleryItems: page.galleryPreviewPhotos,
            goToGallery,
            featuredVideo: page.galleryPreviewVideo
        }
    }
})
</script>

<style lang="scss">
.btn-primary {
    background: var(--theme-blue-dark);
    cursor: pointer;
    color: white;

    &:hover {
        color: black;
        background: var(--theme-blue-light);
    }
}
</style>