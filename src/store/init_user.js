import {default as axios} from "axios";
import {Device} from '@capacitor/device';
import host from "@/host";


export default async function () {
    console.log('init user')
    const device_info = JSON.stringify(await Device.getInfo());
    const res = await axios.get(`${host}/new_user`, {params: {device_info}})

    return res.data.token
}