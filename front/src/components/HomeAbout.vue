<template>
    <div
         class="first-row__wrapper max-w-7xl mx-auto bg-white rounded-lg p-2 sm:p-4 md:p-6 max-w-6xl mx-auto my-4 sm:my-6 md:my-8">
        <div class="first-row">
            <div
                 class="first-row__date text-center text-theme-blue-dark text-base sm:text-lg md:text-xl font-medium mb-1 sm:mb-2">
                <div>{{ pageDate }}</div>
            </div>
            <div
                 class="first-row__title text-2xl sm:text-3xl md:text-4xl mt-4 sm:mt-6 md:mt-10 text-center font-bold text-theme-black mb-2 sm:mb-3 md:mb-4">
                {{ pageTitle }}
            </div>
            <div
                 class="first-row__description text-center text-theme-grey-blue text-base sm:text-lg md:text-xl mb-4 sm:mb-6 md:mb-8">
                {{ place }}
            </div>

            <div
                 class="first-row__about-blocks grid mt-8 sm:mt-12 md:mt-20 items-center grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                <div v-for="block in blocks"
                     :key="'aboutBlock' + block.id"
                     class="first-row__about-blocks__block h-full bg-gray-50 max-w-full p-3 sm:p-4 md:p-5 rounded-md border-theme-blue-light shadow-md transition-shadow duration-300">
                    <h2
                        class="first-row__about-blocks__block__title text-theme-blue-dark font-bold text-xl sm:text-2xl mb-1 sm:mb-2">
                        {{ block.title }}
                    </h2>
                    <h3 v-html="block.text"
                        class="first-row__about-blocks__block__description text-base sm:text-lg md:text-xl text-theme-grey-blue text-wrap">
                    </h3>
                </div>
            </div>
        </div>
    </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue'
import { page } from '@/assets/data'
export default defineComponent({
    name: 'AboutInfo',
    setup() {
        return {

            pageTitle: page.title,
            pageDate: page.date,
            place: page.address,
            blocks: page.AboutBlocks
        }
    }
})
</script>

<style scoped>
.text-theme-grey-blue {
    color: var(--theme-grey-blue);
}

.text-theme-blue-light {
    color: var(--theme-blue-light);
}

.text-theme-blue-dark {
    color: var(--theme-blue-dark);
}

.text-theme-black {
    color: var(--theme-black);
}

.text-theme-orange {
    color: var(--theme-orange);
}

.border-theme-blue-light {
    border-color: var(--theme-blue-light);
}

.first-row__about-blocks__block:hover {
    border-color: var(--theme-orange);
}

@media (max-width: 768px) {
    .first-row__title {
        font-size: 1.75rem;
    }

    .first-row__description {
        font-size: 1rem;
    }
}
</style>
