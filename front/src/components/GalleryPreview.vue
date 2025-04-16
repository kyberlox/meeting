<template>
    <div class="printed-container">
        <div class="gallery-preview__wrapper mb-10 p-2 max-w-7xl printed-container mx-auto">
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
            <!--  -->
            <div class="gallery-years mt-8">
                <h3 class="text-2xl font-bold text-center text-theme-blue-dark mb-4">Архив событий за</h3>
                <div class="gallery-years__links flex justify-center flex-wrap gap-4">
                    <button v-for="year in galleryYears"
                            :key="year"
                            @click="goToGallery(year)"
                            class="btn-year cursor-pointer duration-300 text-xl shadow-sm hover:shadow-md py-2 px-6 rounded-md transition-colors bg-theme-blue-dark text-white duration-300 shadow-sm hover:shadow-md">
                        {{ year }}
                    </button>
                </div>
            </div>
            <!--  -->
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
        const goToGallery = (year: string) => {
            router.push(`/archive/${year}`).then(() => {
                window.scrollTo(0, 0);
            });
        }
        return {
            // galleryTitle: page.galleryPreviewTitle,
            galleryItems: page.galleryPreviewPhotos,
            goToGallery,
            featuredVideo: page.galleryPreviewVideo,
            galleryYears: Object.keys(page.archiveTopImg)
        }
    }
})
</script>

<style lang="scss">
.btn-year {
    background: var(--theme-blue-dark);
    cursor: pointer;
    color: white;

    &:hover {
        color: black;
        background: var(--theme-blue-light);
    }
}
</style>