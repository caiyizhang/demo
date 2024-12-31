<template>
    <div class="fixed inset-0 flex items-center justify-center">
        <div class="bg-white w-96 p-6 z-50">
            <h2 class="font-bold text-xl mb-4">{{user.uid ? 'Edit User' : 'Add User'}}</h2>
            <div class="mb-4">
                <label for="name" class="block text-sm font-medium">Name:</label>
                <input type="text" id="name" v-model="user.name" class="w-full border rounded p-2">
            </div>
            <div class="mb-4">
                <label for="name" class="block text-sm font-medium">Gender:</label>
                <select id="gender" v-model="user.gender" class="w-full border rounded p-2">
                    <option value="男">男</option>
                    <option value="女">女</option>
                </select>
            </div>
            <div class="flex justify-end">
                <button class="text-white bg-gray-300 hover:bg-gray-500 p-2 mr-4" @click="closeModal">cancel</button>
                <button class="text-white bg-blue-500 hover:bg-blue-700 p-2" @click="handleAddOrEdit">confirm</button>
            </div>
        </div>
        <div class="absolute inset-0 bg-black opacity-50" @click="closeModal"></div>
    </div>
</template>
<script setup>
import { addUser ,editUser} from '@/api';
import { ref } from 'vue';
const props = defineProps({
    isOpen:Boolean,
    user:Object
})
const emits = defineEmits(['update:isOpen',"update:user",'refresh'])


const handleAddOrEdit =async ()=>{
    try {
        if(props.user.uid){
            let res = await editUser(props.user)
        }else{
            let res = await addUser(props.user)
        }
    } catch (error) {
        console.log(error)
    } finally {
        closeModal()
        emits('refresh')
    }
}
const closeModal = ()=>{
    Object.assign(props.user,{
        name:'',
        gender:'',
        uid:null
    })
    emits('update:isOpen',false)
}   
</script>