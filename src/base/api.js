import host from "@/host";

export default {
    name: 'APIMixin',
    computed: {
        host() {
            return host
        },
        uid() {
            return this.$store.state.uid
        },
        headers() {
            let token = this.$store.state.token
            return {'Authorization': `Bearer ${token}`}
        }
    },
    methods: {
        sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
    }
}