<template>
    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroups">
        <DownOutlined v-if="showGroups" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-2xl p-4">Nhóm</h1>
    </div>

    <div v-show="showGroups">
        <Group :cards="cards" />
    </div>

</template>

<script>
import Group from '../../../components/group/Group.vue'
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";

export default {
    components: { Group, DownOutlined, RightOutlined },
    data() {
        return {
            showGroups: true,
            cards: [
                { id: 1, title: 'Lập trình mạng', description: '21Nh16' },
                { id: 2, title: 'Nhúng', description: '21Nh99' },
            ]
        }
    },
    methods: {
        toggleGroups() {
            this.showGroups = !this.showGroups;
        }
    }
}
</script>