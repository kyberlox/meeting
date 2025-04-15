<template>
  <HeaderMos @scrollToEl="(x) => handleScroll(x)" />

  <main>
    <RouterView :scrollTarget=scrollTarget />
  </main>

  <FooterV />
</template>

<script lang="ts">
import HeaderMos from "@/components/LayoutHeader.vue";
import FooterV from "@/components/LayoutFooter.vue";
import { defineComponent, ref } from 'vue';
import { useRoute, useRouter } from "vue-router";
export default defineComponent({
  components: {
    HeaderMos,
    FooterV
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const scrollTarget = ref(<null | string>null);

    const handleScroll = (section: string) => {
      console.log(route.name);
      console.log(section);

      if ((section == 'participants' || section == 'contacts') && route.name !== 'home') {
        router.push({ name: 'home' }).then(() => {
          scrollTarget.value = section;
        });
      }
      else {
        scrollTarget.value = section;
      }

      setTimeout(() => {
        scrollTarget.value = null;
      }, 1000);
    }
    return {
      scrollTarget,
      handleScroll
    }
  }
})
</script>