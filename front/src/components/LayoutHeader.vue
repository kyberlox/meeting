<template>
    <header>
        <div class="header bg-white shadow-md">
            <div
                 class="header__wrapper max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-4 flex flex-col sm:flex-row justify-between items-center">
                <div class="header__logo__wrapper mb-3 sm:mb-0">
                    <RouterLink to="/"
                                class="header__logo">
                        <img src="@/assets/logo.png"
                             alt="logo"
                             class="h-8 sm:h-10 md:h-12 w-auto">
                    </RouterLink>
                </div>
                <nav class="w-full sm:w-auto">
                    <ul
                        class="header__navbar flex flex-wrap justify-center sm:justify-end items-center space-x-2 sm:space-x-4 md:space-x-8">
                        <li v-for="(nav) in navbarLinks"
                            :key="'nav' + nav.id"
                            class="header__navbar__item cursor-pointer my-1">
                            <div v-if="!nav.subpoints"
                                 :to="nav.route"
                                 @click="handleScrollTabs(nav.route)"
                                 class="text-theme-grey-blue hover:text-theme-blue-dark font-medium transition-colors duration-200 text-sm sm:text-base px-2 py-1 rounded hover:bg-gray-100"
                                 active-class="text-theme-blue-dark font-bold border-b-2 border-theme-orange">
                                {{ nav.title }}
                            </div>
                            <div v-else
                                 class="relative group"
                                 @mouseenter="handleSubpoints(true, nav.id)"
                                 @mouseleave="handleSubpoints(false, nav.id)">
                                <div
                                     class="text-theme-grey-blue hover:text-theme-blue-dark font-medium transition-colors duration-200 text-sm sm:text-base px-2 py-1 rounded hover:bg-gray-100 cursor-pointer flex items-center">
                                    {{ nav.title }}
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                         class="h-3 w-3 sm:h-4 sm:w-4 ml-1"
                                         fill="none"
                                         viewBox="0 0 24 24"
                                         stroke="currentColor">
                                        <path stroke-linecap="round"
                                              stroke-linejoin="round"
                                              stroke-width="2"
                                              d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                                <div :class="{ 'opacity-100': subPointActive && activeIndex == nav.id }"
                                     class="absolute opacity-0 left-0 w-full bg-white rounded-md shadow-lg z-10">
                                    <RouterLink v-for="point in nav.subpoints"
                                                :key="point + 'archive'"
                                                :to="`/archive/${point}`"
                                                class="block rounded-sm px-3 sm:px-4 py-1 sm:py-2 text-xs sm:text-sm text-theme-grey-blue hover:text-theme-blue-dark hover:bg-gray-100"
                                                active-class="text-theme-blue-dark font-bold border-l-2 border-theme-orange bg-gray-50">
                                        {{ point }}
                                    </RouterLink>
                                </div>
                            </div>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { RouterLink } from 'vue-router';
import { navbarLinks } from "@/assets/data";
export default defineComponent({
    name: "HeaderMos",
    emits: ['scrollToEl'],
    setup(props, { emit }) {
        const activeIndex = ref();

        const subPointActive = ref(false);
        const handleSubpoints = (value: boolean, id: number) => {
            subPointActive.value = value;
            activeIndex.value = id;
        }

        const handleScrollTabs = (route: string) => {
            emit('scrollToEl', route);
        }

        return {
            navbarLinks,
            subPointActive,
            handleSubpoints,
            activeIndex,
            handleScrollTabs
        }
    }
})
</script>

<style lang="scss" scoped>
#app {
    max-width: 1200px;
    margin: auto;
    padding: 10px;
}

.header {
    position: sticky;
    top: 0;
    z-index: 50;
    border-bottom: 1px solid #f0f0f0;
}

.header__logo {
    transition: transform 0.2s ease;

    &:hover {
        transform: scale(1.05);
    }
}

.text-theme-grey-blue {
    color: var(--theme-grey-blue);
}

.text-theme-blue-dark {
    color: var(--theme-blue-dark);
}

.border-theme-orange {
    border-color: var(--theme-orange);
}


.nav--active+.subnav {
    display: flex;
}

@media (max-width: 640px) {
    .header__navbar {
        width: 100%;
        justify-content: center;
    }
}
</style>
