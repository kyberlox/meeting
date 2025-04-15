<template>
    <div v-if="modalOpen"
         class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="absolute inset-0 modal-fade"
             @click="closeModal"></div>

        <div class="relative z-10 max-w-[90vw] max-h-[90vh] overflow-hidden">
            <div class="relative">
                <img :src="modalImage"
                     class="max-h-[90vh] max-w-[90vw] object-contain" />
                <CloseIcon class="hover:opacity-50 transition cursor-pointer absolute top-2 right-2 z-20 w-14 flex items-center justify-center rounded-full"
                           @click="closeModal" />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import CloseIcon from "@/assets/icons/CloseIcon.vue";
import { defineComponent, ref } from "vue";

export default defineComponent({
    props: {
        modalImage: {
            type: String,
            required: true,
        },
        modalOpen: {
            type: Boolean,
            default: false,
        },
    },
    components: {
        CloseIcon
    },
    emits: ['closeModal'],
    setup(props, { emit }) {
        const closeModal = () => {
            emit('closeModal');
        };

        return {
            closeModal,
        };
    },
})
</script>

<style lang="scss" scoped>
.modal-fade {
    background-color: rgba(0, 0, 0, 0.85);
}
</style>
