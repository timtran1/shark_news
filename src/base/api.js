export default {
    name: 'APIMixin',
    computed: {
        host() {
            if (process.env.NODE_ENV === 'development') return 'http://localhost'
            return ''
        }
    }
}