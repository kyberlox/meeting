<template>
    <div class="archieve__wrapper"
         v-if="title">
        <div class="w-full max-h-120 h-auto bg-no-repeat bg-cover bg-center rounded-md aspect-16/9 bg-position-[center_top_55%]"
             :style="{ 'background-image': `url(${topPhoto})` }">
        </div>
        <div @click="navArchiveOpen = !navArchiveOpen"
             class="archieve__title text-4xl mt-20 text-center font-bold text-theme-dark mb-4 flex flex-row gap-2 justify-center items-center content-center">
            Как это было в <span
                  class="text-theme-orange relative flex flex-row cursor-pointer hover:text-theme-blue-dark transition-colors duration-300 justify-center items-center content-center group">{{
                    title
                }}
                <svg xmlns="http://www.w3.org/2000/svg"
                     class="relative h-6 w-6 sm:h-7 sm:w-7 md:h-8 md:w-8 ml-1 group-hover:scale-110 transition-transform duration-300"
                     fill="none"
                     viewBox="0 0 24 24"
                     stroke="currentColor">
                    <path stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M19 9l-7 7-7-7" />
                </svg>

                <div v-if="navArchiveOpen"
                     class="absolute opacity-100 top-full right-0 w-full bg-white rounded-md shadow-lg z-10 mt-1 transform origin-top-right transition-all duration-200 ease-in-out animate-dropdown">
                    <RouterLink v-for="point in navArchive"
                                :key="point + 'archive'"
                                :to="`/archive/${point}`"
                                class="block rounded-sm px-3 sm:px-4 py-1 sm:py-2 text-xs sm:text-sm text-theme-grey-blue hover:text-theme-blue-dark hover:bg-gray-100"
                                active-class="text-theme-blue-dark font-bold border-l-2 border-theme-orange bg-gray-50">
                        {{ point }}
                    </RouterLink>
                </div>
            </span>

        </div>
        <div
             class="archieve__content cursor-pointer mx-auto max-w-7xl gap-5 my-20 grid grid-cols-1 px-2 sm:grid-cols-2 md:grid-cols-3 justify-items-center  row-auto">
            <div v-for="(i) in images"
                 @click="openModal(i)"
                 :key="i + 'photoIndex'"
                 class="archieve__content-item w-full">
                <div class="archieve__content-item__video__wrapper relative"
                     v-if="i?.includes('mp4')">
                    <div class="video-container">
                        <video ref="videoPlayer"
                               class="video-js rounded-md vjs-default-skin vjs-big-play-centered"
                               controls
                               preload="auto"
                               width="100%"
                               height="100%"
                               poster=""
                               data-setup="{autoplay: true}"
                               @play="isPlaying = true"
                               @pause="isPlaying = false"
                               @ended="isPlaying = false">>
                            <source :src="i"
                                    type="video/mp4" />
                            <p class="vjs-no-js">
                                Для просмотра видео включите JavaScript и обновите браузер до
                                <a href="https://videojs.com/html5-video-support/"
                                   target="_blank">
                                    поддерживающего HTML5 видео
                                </a>
                            </p>
                        </video>
                    </div>
                    <PlayIcon v-if="!isPlaying"
                              class="play-icon hover:scale-101 pointer-events-none" />
                </div>
                <div v-else
                     @click="openModal(i)"
                     class="w-full h-auto bg-no-repeat bg-cover bg-center rounded-md aspect-16/9 transition-all ease-in-out duration-300 hover:scale-105 hover:shadow-lg aspect-16/9"
                     :style="{ 'background-image': `url(${i})` }">
                </div>
            </div>
        </div>
        <GalleryModal :modalOpen="modalOpen"
                      :modalImage="modalImage"
                      @closeModal="modalOpen = false" />

    </div>
</template>


<script lang="ts">
import { defineComponent, ref, computed } from "vue";
import PlayIcon from "@/assets/icons/PlayIcon.vue";
import { page } from "@/assets/data";
import GalleryModal from '@/components/GalleryModal.vue'

export default defineComponent({
    name: 'ArchieveView',
    components: {
        PlayIcon,
        GalleryModal
    },
    props: {
        title: {
            type: String,
            required: true
        }
    },
    setup(props) {
        const videoPlayer = ref(null);
        const modalOpen = ref(false);
        const modalImage = ref();

        const topPhoto = computed(() => {
            const key = props.title as unknown as keyof typeof page.archiveTopImg;
            return page.archiveTopImg[key];
        })

        const images = computed(() => {
            const key = props.title as unknown as keyof typeof page.gallery;
            return page.gallery[key] || [];
        });
        const isPlaying = ref(false);

        const openModal = (url: string) => {
            if (url.includes('mp4')) return;

            modalOpen.value = true;
            modalImage.value = url;
        }

        const navArchiveOpen = ref(false);

        return {
            videoPlayer,
            isPlaying,
            images,
            topPhoto,
            openModal,
            modalOpen,
            modalImage,
            navArchive: Object.keys(page.archiveTopImg),
            navArchiveOpen
        }
    }
})
</script>

<style lang="scss" scoped>
.playBtn {
    width: 30%;
    height: 30%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10;
}

.video-container:hover {
    .play-icon {
        transform: scale(1.01);
        display: none;
    }
}

.text-theme-orange {
    color: var(--theme-orange);
    transition: color 0.3s ease;

    &:hover {
        color: var(--theme-blue-dark);
    }
}

@keyframes dropdown {
    from {
        opacity: 0;
        transform: scale(0.95) translateY(-10px);
    }

    to {
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}

.animate-dropdown {
    animation: dropdown 0.2s ease-out forwards;
}
</style>
