<template>
    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroup1">
        <DownOutlined v-if="showGroup1" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Nhóm</h1>
    </div>

    <div v-show="showGroup1" class="scroll-container">
        <Group :cards="cards" />
    </div>

    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroup2">
        <DownOutlined v-if="showGroup2" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Nhóm đã ẩn</h1>
    </div>
    <div v-show="showGroup2" class="scroll-container">
        <Group :cards="cards" />
    </div>

    <router-view />
</template>

<script>
import Group from '../../../components/group/Group.vue'
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";

export default {
    components: { Group, DownOutlined, RightOutlined },
    data() {
        return {
            showGroup1: true,
            showGroup2: false,
            cards: [
                { id: 1, title: 'Lập trình mạng', description: '21Nh16' },
                { id: 2, title: 'Nhúng', description: '21Nh99' },
            ]
        }
    },
    methods: {
        toggleGroup1() {
            this.showGroup1 = !this.showGroup1;
        },
        toggleGroup2() {
            this.showGroup2 = !this.showGroup2;
        }
    }
}
</script>
<style>
.scroll-container {
    max-height: 80vh; /* Adjust this value to fit your needs */
    overflow-y: auto;
}
</style>