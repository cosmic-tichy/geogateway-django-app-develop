<template>

    <div class="window">
        <b-navbar id="top" toggleable="lg" type="dark" variant="dark">
                <img id="logo" src="../assets/logo.png" alt="GeoGateway Logo">
            <b-button v-b-toggle.sidebar-1>
                <b-icon-wrench></b-icon-wrench>
            </b-button>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        </b-navbar>
    </div>

</template>

<script>
    // import ToolBar from "./ToolBar";
    export default {
        name: "TopNav",
        components: {
            // ToolBar
        }
    }
</script>

<style scoped>
#logo {
    position: absolute;
    left: 50%;
    margin-left: -10px;
    float: top;
    height: 40px;
    width: 110px;
}
</style>