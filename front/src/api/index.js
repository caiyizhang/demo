import request from "@/utils/request"

export const getUserList = ()=>{
    return request({
        url:'/api/get_user_list',
        method:'get'
    })
}

export const addUser = (data)=>{
    return request({
        url:'/api/add_user',
        method:'post',
        data
    })
}

export const editUser = (data)=>{
    return request({
        url:`/api/edit_user/${data.uid}`,
        method:'put',
        data
    })
}