import {actionSheetController, alertController} from '@ionic/vue';

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
                    cssClass: 'my-custom-class',
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
                    // header: 'Albums',
                    cssClass: 'my-custom-class',
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
                                console.log('Share clicked')
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
                    // header: 'Albums',
                    cssClass: 'my-custom-class',
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
                                console.log('Share clicked')
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