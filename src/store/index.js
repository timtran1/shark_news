import {createStore} from 'vuex'
import {Storage} from '@capacitor/storage';
import init_user from "./init_user";

export default async function init_store() {
    let [token, uid] = await Promise.all([
        Storage.get({key: 'token'}),
        Storage.get({key: 'v_uid'})
    ])

    token = token.value || await init_user()
    uid = parseInt(uid.value)

    return createStore({
        state() {
            return {
                uid,
                token,
                reporting_comment: null,
                reporting_post: null,
                reporting: '',
                writing_report: false,
            }
        },
        mutations: {
            set_token(state, token) {
                Storage.set({
                    key: 'token',
                    value: token
                })
                state.token = token
            },
            set_uid(state, uid) {
                Storage.set({
                    key: 'v_uid',
                    value: uid.toString()
                })
                state.uid = uid
            },
        }
    })
}