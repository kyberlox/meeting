<template>
  <DownHeaderPhoto />
  <AboutInfo />
  <HomeMainVideo />
  <GalleryPreview />
  <Partycipants ref=participants />
  <PlaceYMap />
  <Contacts ref=contacts />
</template>

<script lang="ts">
import { defineComponent, ref, watch, computed, onMounted, type ComponentPublicInstance } from 'vue'
import AboutInfo from "@/components/HomeAbout.vue";
import GalleryPreview from "@/components/GalleryPreview.vue";
import PlaceYMap from "@/components/HomeYMap.vue";
import Contacts from "@/components/HomeContacts.vue";
import DownHeaderPhoto from '@/components/HomeMainPhoto.vue';
import Partycipants from '@/components/HomePartycipants.vue';
import HomeMainVideo from '@/components/HomeMainVideo.vue';
import { setSeo } from '@/utils/setSeo'
import { useSeoMeta } from '@unhead/vue'

export default defineComponent({
  components: {
    AboutInfo,
    GalleryPreview,
    PlaceYMap,
    Contacts,
    DownHeaderPhoto,
    Partycipants,
    HomeMainVideo
  },
  props: {
    scrollTarget: {
      type: String
    },
  },
  emits: ['scrollToEl'],
  setup(props, { emit }) {
    onMounted(() => {
      const metaTitle = computed(() => `Главная | Слет проектировщиков`);
      const metaDescription = computed(() => `О нас | Слет проектировщиков`);
      setSeo(metaTitle.value, metaDescription.value, 'about');
    })


    const participants = ref<ComponentPublicInstance | null>(null);
    const contacts = ref<ComponentPublicInstance | null>(null);

    watch(() => props.scrollTarget, (newVal) => {
      if (newVal) {
        scrollTo(newVal);
        emit('scrollToEl', 'ds');
      }
    })

    const scrollTo = (section: string) => {
      if (!section) return;

      const target: HTMLElement | null = section == 'contacts' ? contacts.value?.$el : participants.value?.$el;

      if (!target) return

      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }

    return {
      scrollTo,
      contacts,
      participants,
    }
  }
})
</script>
