<template>
    <div class="printed-container">
        <div class="gallery-preview__wrapper p-2 max-w-7xl printed-container mx-auto">
            <h3 class="gallery-preview__title text-3xl mt-10 text-center font-bold text-theme-blue-dark mb-4">
                {{ galleryTitle }}
            </h3>
            <div v-if="featuredVideo"
                 class="featured-video-container mx-auto px-2  max-w-7xl  ">
                <video-player class="video-player max-w-full vjs-theme-forest video-wrapper cursor-pointer relative rounded-md overflow-hidden shadow-lg transition-all duration-300 hover:shadow-xl w-full!"
                              :src="featuredVideo"
                              controls
                              autoplay
                              playsinline
                              :height=videoHeight
                              :volume="0.6" />
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
        return {
            featuredVideo: page.galleryPreviewVideo,
            galleryTitle: page.galleryPreviewTitle,
            videoHeight: 550,
        }
    }
})
</script>
<style lang="scss" scoped>
.featured-video-container {
    .video-wrapper {
        position: relative;
        transition: all 0.3s ease;

        &:hover {
            transform: scale(1.01);
        }

        &:hover {
            transform: scale(1.01);

            :deep(.vjs-big-play-button) {
                background-color: var(--theme-orange, var(--theme-orange));
            }
        }

        :deep(.vjs-big-play-button) {
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            margin: 0 !important;
            border: 2px solid white;
            background-color: rgba(43, 51, 63, 0.7);
            border-radius: 50%;
            width: 80px;
            height: 80px;
            line-height: 80px;

            &:before {
                font-size: 40px;
                top: 50%;
                left: 50%;
                transform: translate(-40%, -50%);
                position: absolute;
            }
        }
    }
}
</style>