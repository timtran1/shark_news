import {createStore} from 'vuex'
import {Storage} from '@capacitor/storage';
import {default as axios} from "axios";

export default async function init_store() {
    let [token, uid] = await Promise.all([
        Storage.get({key: 'token'}),
        Storage.get({key: 'uid'})
    ])

    token = token.value
    uid = uid.value


    if (!token) {
        const host = process.env.NODE_ENV === 'development' ? 'http://localhost' : ''
        let res = await axios.get(`${host}/new_user`)
        token = res.data.token

        await Storage.set({
            key: 'token',
            value: token
        })
    }

    return createStore({
        state() {
            return {
                uid,
                token
            }
        },
        mutations: {
            set_token(state, token) {
                state.token = token
            },
            set_uid(state, uid) {
                state.token = uid
            },
        }
    })
}