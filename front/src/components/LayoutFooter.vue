<template>
    <footer>
        <div class="footer__wrapper  p-5">
            <div class="footer flex text-sm flex-col items-center justify-center pb-2">
                <div class="footer-copyright mt-0.5">{{ copyright }}</div>
                <div class="footer-email mt-0.5">{{ email }}</div>
                <div class="footer-phone mt-0.5">{{ phone }}</div>
                <div class="footer-phone mt-0.5">{{ phoneInner }}</div>
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

<style>
.footer__wrapper {
    background: black;
}

.footer {
    color: #666;
    font-weight: 600;
}

.footer-phone {
    color: var(--theme-orange);
}
</style>