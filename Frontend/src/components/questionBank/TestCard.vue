<template>

    <div class="bg-white shadow-xl rounded-xl p-6 w-64 h-auto m-4 flex flex-col">
        <h2 class="text-2xl font-semibold mb-4">{{ test.name }}</h2>
        <p class="font-bold">Bắt đầu: </p>
        <p class="text-gray-700">{{formatDate( test.start) }}</p>
        <p class="font-bold">Kết thúc: </p>
        <p class="text-gray-700">{{ formatDate(test.end) }}</p>
        <p class="font-bold">Thời gian làm bài: </p>
        <p class="text-gray-700">{{ test.duration }} phút</p>
        <a-button v-if="isStudentRoute" @click="showConfirm" class=" bg-blue-500 text-white rounded-md">Bắt đầu làm
            bài</a-button>
    </div>
</template>

<script>
import { format } from 'date-fns';
import { useRouter } from 'vue-router';
import { Modal } from 'ant-design-vue';
import { h } from 'vue';
import { ExclamationCircleOutlined } from '@ant-design/icons-vue';
import { useStudentStore } from '../../stores/modules/student';
export default {
    props: {
        test: {
            type: Object,
            required: true
        },

    },
    setup(props) {
        const studentStore = useStudentStore();
        const router = useRouter();
        const isStudentRoute = router.currentRoute.value.path.startsWith('/student');
        const formatDate = (date) => {
            return format(new Date(date), 'dd/MM/yyyy - HH:mm');
        }
        const showConfirm = () => {
            Modal.confirm({
                title: 'Bạn có chắc chắn vào thi ngay bây giờ?',
                icon: h(ExclamationCircleOutlined),
                content: h(
                    'div',
                    {
                        style: 'color:red;',
                    },
                    'Khi bắt đầu làm bài, bạn không được chuyển tab hay sử dụng các phím tắt. Nếu bị phát hiện chuyển tab trong lúc làm bài. Bài thi sẽ dừng ngay lập tức và bạn sẽ bị 0 điểm',
                ),
                onOk() {
                    const width = window.screen.width;
                    const height = window.screen.height;
                    studentStore.group_test_id = props.test.id;
                    // console.log(studentStore.group_test_id)
                    window.open('/test', '_blank', `width=${width},height=${height}`);
                },
                onCancel() {
                    console.log('Cancel');
                },
                okText: "Vào thi",
                cancelText: "Hủy",
                class: 'test',
            });
        };

        return {
            router,
            isStudentRoute,
            showConfirm,
            formatDate
        }
    }
}
</script>

<style>

</style>