export default {
    name: 'APIMixin',
    computed: {
        host() {
            if (process.env.NODE_ENV === 'development') return 'http://localhost'
            return 'https://api.sharknews.live'
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