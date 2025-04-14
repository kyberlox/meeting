<template>
    <div class="printed-container mt-10 sm:mt-16 md:mt-20">
        <div class="contacts__wrapper max-w-7xl mx-auto printed-container px-4 sm:px-6">
            <div class="contacts py-6 sm:py-8 md:py-10">
                <div
                     class="contacts__title text-base sm:text-lg md:text-xl max-w-xs sm:max-w-sm md:max-w-md m-auto text-center">
                    По вопросам участия и любым другим вопросам свяжитесь с нами:
                </div>
                <div
                     class="contacts__text flex flex-col justify-center gap-1 sm:gap-2 text-lg sm:text-xl md:text-2xl max-w-xs sm:max-w-sm md:max-w-md m-auto text-center mt-3 sm:mt-4 md:mt-5">
                    <span class="break-words"> {{ phone }}</span>
                    <span class="break-words"> {{ phoneInner }}</span>
                    <span class="mt-1 sm:mt-2 break-words"> {{ email }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { page } from '@/assets/data'
export default defineComponent({
    setup() {
        return {
            phone: page.phone,
            email: page.email,
            phoneInner: page.phoneInner
        }
    }
})
</script>

<style scoped>
.contacts {
    color: var(--theme-blue-dark);
}

.contacts__text {
    font-weight: 600;
}

@media (max-width: 640px) {
    .contacts__text {
        word-break: break-word;
    }
}
</style>
