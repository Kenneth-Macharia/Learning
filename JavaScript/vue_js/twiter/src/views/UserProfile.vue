<template>
  <div class="user-profile">
    <div class="user-profile_sidebar">
      <div class="user-profile_user-panel">
        <h1 class="user-profile_uname">@{{ state.user.username }}</h1>
        <div class="user-profile_admim-badge"
            v-if="state.user.isAdmin">
            Admin
        </div>
        <div class="user-profile_fcount">
            <strong>Followers: </strong>{{ state.followers }}
        </div>
      </div>
        <!-- CreateNewTwit panel component -->
        <CreateTwitPanel @add-twit="addTwit"/>
    </div>

    <div class="user-profile_twit-wrapper">
      <!-- TwitItem component -->
      <TwitItem class="user-profile_twit"
        v-for="twit in state.user.twits"
        :key="twit.id"
        :username="state.user.username"
        :twit="twit"
        @favourite="toggleFavourite"/>

    </div>
  </div>
</template>

<script>
import { reactive, computed, watchEffect } from "vue"
import { useRoute } from "vue-router"
import TwitItem from "../components/TwitItem"
import CreateTwitPanel from "../components/CreateTwitPanel"
import { usersObj } from "../assets/users"

export default {
  name: 'UserProfile',
  components: {
    TwitItem,
    CreateTwitPanel
  },
  setup() {
    const route = useRoute()
    const userId = computed(() => route.params.userId)

    const state = reactive({
      followers: 0,
      user: usersObj[(userId.value) - 1] || usersObj[0]
    })

    const followers = watchEffect((newCount, oldCount) => {
      // watches triggers when a properties changes & should be named after the property being watched
      if (oldCount < newCount) {
        console.log(`${state.user.username} has gained a new follower!`)
      }
    })

    function toggleFavourite(id) {
      console.log(`Favourite twit is #${id}`)
    }

    function addTwit(twit) {
      state.user.twits.unshift(
        {
          id: state.user.twits.length + 1,
          content: twit
        }
      )
    }

    return {
      state,
      userId,
      followers,
      toggleFavourite,
      addTwit
    }
  }
}
</script>

<style lang="scss" scoped>
.user-profile {
    display: grid;
    grid-template-columns: 1fr 3fr;
    grid-gap: 50px;
    padding: 50px 5%;

    .user-profile_user-panel {
      display: flex;
      flex-direction: column;
      padding: 20px;
      background-color: white;
      border: 1px solid #dfe3eb;
      border-radius: 5px;
      margin-bottom: auto;

      .user-profile_admim-badge {
        background-color: rebeccapurple;
        color: white;
        border-radius: 5px;
        margin-right: auto;
        padding: 0 10px;
        font-weight: bold;
      }

      h1 {
        margin: 0;
      }

      .user-profile_create_twit {
        display: flex;
        flex-direction: column;
        padding-top: 20px;

        &.exceeded {
          color: red;
        }
      }

      .user-profile_twit-wrapper {
        display: grid;
        grid-gap: 10px;
        margin-bottom: auto;
      }
  }
}
</style>
