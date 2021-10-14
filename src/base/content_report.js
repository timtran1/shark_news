import {actionSheetController, alertController, loadingController} from '@ionic/vue';
const axios = require("axios").default


export default {
    name: 'ContentReportMixin',
    data() {
        return {
            reasons: [
                'Nudity',
                'Violence',
                'Harassment',
                'Suicide or self-harm',
                'False information',
                'Spam',
                'Hate speech',
                'Other'
            ],
            reason_value: '',
            reason_other: '',
        }
    },
    computed: {
        writing_report() {
            return this.$store.state.writing_report
        }
    },
    methods: {
        async block(user) {
            const loading = await loadingController
                .create({
                    message: 'Blocking...',
                    duration: 2000
                });
            await loading.present();
            await axios.get(`${this.host}/block?user_id=${user.id}`,{
                headers: this.headers
            })
            loading.dismiss()
        },
        async confirm_block(user) {
            if (!this.uid) {
                this.$router.push('/auth')
                return
            }

            const alert = await alertController
                .create({
                    header: `Block ${user.name}?`,
                    message: 'They will no longer be able to see or interact with your posts and comments. You will also no longer see their posts on your feed.',
                    buttons: [
                        {
                            text: 'Cancel',
                            role: 'cancel',
                        },
                        {
                            text: 'Block',
                            handler: () => {
                                this.block(user)
                            }
                        },
                    ],
                });
            return alert.present();
        },
        toggle_write_report() {
            this.$store.state.writing_report = !this.$store.state.writing_report
        },
        write_report() {
            if (!this.uid) {
                this.$router.push('/auth')
                return
            }
            this.toggle_write_report()
        },
        async report_sent() {
            this.toggle_write_report()
            const alert = await alertController
                .create({
                    header: 'Report sent!',
                    message: 'Thank you for helping us keep SharkNews clean for you and your fellow sharks. We will be looking into your report, and let you know by email if actions are taken.',
                    buttons: ['OK'],
                });
            return alert.present();
        },
        async more_actions_comment(comment) {
            this.$store.state.reporting_comment = comment
            this.$store.state.reporting = 'comment'
            const actionSheet = await actionSheetController
                .create({
                    buttons: [
                        {
                            text: 'Report',
                            role: 'destructive',
                            handler: this.write_report,
                        },
                        {
                            text: 'Block user',
                            role: 'destructive',
                            handler: () => {
                                this.confirm_block(comment.user)
                            },
                        },
                        {
                            text: 'Cancel',
                            role: 'cancel',
                        },
                    ],
                });
            await actionSheet.present();

            const {role} = await actionSheet.onDidDismiss();
            console.log('onDidDismiss resolved with role', role);
        },
        async more_actions_post(post) {
            console.log({post})
            this.$store.state.reporting_post = post
            this.$store.state.reporting = 'post'
            const actionSheet = await actionSheetController
                .create({
                    buttons: [
                        {
                            text: 'Report',
                            role: 'destructive',
                            handler: this.write_report,
                        },
                        {
                            text: 'Block user',
                            role: 'destructive',
                            handler: () => {
                                this.confirm_block(post.user)
                            },
                        },
                        {
                            text: 'Cancel',
                            role: 'cancel',
                        },
                    ],
                });
            await actionSheet.present();

            const {role} = await actionSheet.onDidDismiss();
            console.log('onDidDismiss resolved with role', role);
        },
    }
}