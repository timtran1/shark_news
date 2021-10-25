import {createRouter, createWebHistory} from '@ionic/vue-router';
import Tabs from '../views/Tabs.vue'
import Feed from "../views/Feed";
import Profile from "../views/Profile";
import AuthOptions from "../components/AuthOptions";
import SignUp from "../components/SignUp";
import Login from "../components/Login";
import PostDiscussionView from "../components/PostDiscussionView";
import PostWebView from "../components/PostWebView";
import Add from "../views/Add";

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
                component: Feed
            },
            {
                path: 'add',
                component: Add
            },
            {
                path: 'profile',
                component: Profile
            },
        ]
    },
    {
        path: '/auth',
        component: AuthOptions,
        props: {
            show_header: true,
            return_after_auth: true
        }
    },
    {
        path: '/signup',
        component: SignUp
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/post/view/:id',
        component: PostWebView
    },
    {
        path: '/post/discussion/:id',
        component: PostDiscussionView
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
