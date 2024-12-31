<template>
    <div>
        <button class="rounded text-white bg-blue-500 hover:bg-blue-700 mb-4" @click="handleOpen">Add User</button>
        <div class="w-[500px]">
            <table class="border w-full border-collapse text-center">
                <thead>
                    <tr>
                        <th class="py-2 px-4 border">ID</th>
                        <th class="py-2 px-4 border">Name</th>
                        <th class="py-2 px-4 border">Gender</th>
                        <th class="py-2 px-4 border">Edit</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in userList" :key="user.uid">
                        <td class="py-2 px-4 border">{{user.uid}}</td>
                        <td class="py-2 px-4 border">{{user.name}}</td>
                        <td class="py-2 px-4 border">{{user.gender}}</td>
                        <td class="py-2 px-4 border">
                            <button class="rounded text-white px-2 py-1 bg-green-500 hover:bg-green-700" @click="handleOpen(user)">edit</button>
                        </td>
                    </tr>
                </tbody>

            </table>
        </div>
        <Modal v-if="isOpen" v-model:isOpen="isOpen" v-model:user="user" @refresh="getData"/>
    </div>
</template>

<script setup>
import { onBeforeMount, reactive, ref } from 'vue';
import Modal from './component/Modal.vue';
import {getUserList} from "@/api/index"
const isOpen = ref(false)
const userList = ref([])
const user =  reactive({
    name:'',
    gender:''
})
onBeforeMount(()=>{
    getData()
})

const getData =async ()=>{
    let res = await getUserList()
    userList.value = res
}

const handleOpen = (item={})=>{
    Object.assign(user,item)
    isOpen.value = true
}

</script>