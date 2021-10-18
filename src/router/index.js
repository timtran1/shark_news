import {createRouter, createWebHistory} from '@ionic/vue-router';
import Tabs from '../views/Tabs.vue'

const routes = [
    {
        path: '/',
        redirect: '/tabs/feed'
    },
    {
        path: '/tabs/',
        component: Tabs,
        children: [
            {
                path: '',
                redirect: '/tabs/feed'
            },
            {
                path: 'feed',
                component: () => import('@/views/Feed.vue')
            },
            {
                path: 'add',
                component: () => import('@/views/Add.vue')
            },
            {
                path: 'profile',
                component: () => import('@/views/Profile.vue')
            },
        ]
    },
    {
        path: '/auth',
        component: () => import('@/components/AuthOptions.vue'),
        props: {
            show_header: true,
            return_after_auth: true
        }
    },
    {
        path: '/signup',
        component: () => import('@/components/SignUp.vue')
    },
    {
        path: '/login',
        component: () => import('@/components/Login.vue')
    },
    {
        path: '/post/view/:id',
        component: () => import('@/components/PostWebView.vue')
    },
    {
        path: '/post/discussion/:id',
        component: () => import('@/components/PostDiscussionView.vue')
    },
    {
        path: '/privacy-policy',
        component: () => import('@/info/PrivacyPolicy.vue')
    },
    {
        path: '/terms-and-conditions',
        component: () => import('@/info/Terms.vue')
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
