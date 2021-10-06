import {default as axios} from "axios";

export default async function () {
    const host = process.env.NODE_ENV === 'development' ? 'http://localhost' : 'https://api.sharknews.live'
    let res = await axios.get(`${host}/new_user`)
    return res.data.token
}