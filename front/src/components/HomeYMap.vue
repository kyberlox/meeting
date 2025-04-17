<template>
    <div class="bg-white max-w-7xl px-10 mx-auto w-full rounded-lg mt-20">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-25 items-center">
            <div class="w-full h-[350px] rounded-lg md:col-span-2 overflow-hidden">
                <yandex-map v-model="map"
                            :settings="{
                                location: {
                                    center: staticCoordinates as LngLat,
                                    zoom: 15,
                                },
                            }"
                            class="w-full h-full"
                            width="100%"
                            height="100%">
                    <yandex-map-default-scheme-layer />
                    <yandex-map-default-features-layer />
                    <yandex-map-default-marker :settings="{ coordinates: staticCoordinates as LngLat }">
                        <img alt=""
                             class="pin"
                             :src="'https://mail.emk.ru/skins/larry/images/logo.svg?s=1740566218'" />
                    </yandex-map-default-marker>
                </yandex-map>
            </div>

            <div class="space-y-2 px-4 ml-auto">
                <h2 class="text-3xl font-bold text-theme-blue-dark">{{ place }}</h2>
                <h3 class="text-2xl font-semibold text-theme-black">{{ address }}</h3>
                <p class="text-theme-grey-blue text-lg">
                    {{ street }}
                </p>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import type { LngLat, YMap } from '@yandex/ymaps3-types';
import { shallowRef } from 'vue';
import { page } from '@/assets/data';
import {
    YandexMap,
    YandexMapDefaultSchemeLayer,
    YandexMapDefaultFeaturesLayer,
    YandexMapDefaultMarker
} from 'vue-yandex-maps';

import { defineComponent } from "vue";
export default defineComponent({
    name: 'PlaceYMap',
    components: {
        YandexMap,
        YandexMapDefaultSchemeLayer,
        YandexMapDefaultFeaturesLayer,
        YandexMapDefaultMarker
    },
    setup() {
        const map = shallowRef<null | YMap>(null);

        return {
            place: page.place,
            street: page.street,
            address: page.address,
            map,
            staticCoordinates: [page.coordinatesW, page.coordinatesH],
        }
    }
})
</script>