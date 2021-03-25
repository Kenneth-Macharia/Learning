<template>
    <div class="home">
        <h1>Home Page</h1>
        <div class="users-list">
            <router-link
                v-for="user in usersObj"
                :key="user.id"
                :to="{ name: 'UserProfile', params: { userId: user.id } }">
                    {{ user.username }}
            </router-link>
        </div>
    </div>
</template>

<script>
import { usersObj } from "../assets/users"

export default {
    name: 'Home',
    setup() {
        return {
            usersObj
        }
    }
}
</script>

<style scope lang="scss">
.home {
    padding: 2% 5%;

    .users-list {
        display: flex;
        flex-direction: column;
    }
}
</style>
