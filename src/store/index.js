import {createStore} from 'vuex'
import {Storage} from '@capacitor/storage';
import init_user from "./init_user";

export default async function init_store() {
    let [token, uid] = await Promise.all([
        Storage.get({key: 'token'}),
        Storage.get({key: 'v_uid'})
    ])

    token = token.value
    uid = parseInt(uid.value)

    if (!token) {
        token = await init_user()
        uid = 0
        Storage.set({
            key: 'token',
            value: token
        })
    }

    return createStore({
        state() {
            return {
                uid,
                token,
                reporting_comment: null,
                reporting_post: null,
                reporting: '',
                writing_report: false,
                feed_offset: 0,
                feed_end_reached: false,
                viewing_post_id: false,
                starting_viewing_timestamp: 0
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