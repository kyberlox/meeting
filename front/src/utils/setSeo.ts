import { useSeoMeta } from '@unhead/vue'

export const setSeo = (title: string, description: string, ogTitle: string, ogImage: string = '/galleryPreview/2.jpg') => {
    useSeoMeta({
        title: title,
        description: description,
        ogDescription: description,
        ogTitle: ogTitle,
        ogImage: ogImage,
    })
}