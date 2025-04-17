<template>
    <footer>
        <div class="footer__wrapper text-gray-500 bg-black p-5">
            <div class="footer font-semibold flex text-sm flex-col items-center justify-center pb-2">
                <div class="footer-copyright mt-0.5">{{ copyright }}</div>
                <div class="footer-email mt-0.5">{{ email }}</div>
                <div class="footer-phone text-theme-orange mt-0.5">{{ phone }}</div>
                <div class="footer-phone text-theme-orange mt-0.5">{{ phoneInner }}</div>
            </div>
        </div>
    </footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { page } from '@/assets/data'
export default defineComponent({
    setup() {
        return {
            copyright: new Date().getFullYear() + ' Все права защищены',
            email: page.email,
            phone: page.phone,
            phoneInner: page.phoneInner
        }
    }
})
</script>