import {default as axios} from "axios";
import {Device} from '@capacitor/device';

export default async function () {
    console.log('init user')
    const host = process.env.NODE_ENV === 'development' ? 'http://localhost' : 'https://api.sharknews.live'
    const device_info = JSON.stringify(await Device.getInfo());
    const res = await axios.get(`${host}/new_user`, {params: {device_info}})

    return res.data.token
}