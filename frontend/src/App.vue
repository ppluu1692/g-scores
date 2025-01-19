<template>
    <div class="topbar">
        <div class="topbar-title">
            <h2>G-Scores</h2>
            <h4>2024 National High School Graduation Exam</h4>
        </div>
    </div>
    <div class="main-content">
        <div class="sidebar">
            <h4>MENU</h4>
            <ul>
                <li>
                    <label @click="onTagClicked($event, 0)" :class="currentTab === 0 ? 'active' : ''">
                        <span class="bx bx-objects-horizontal-left"></span>
                        <span>Dashboard</span>
                    </label>
                </li>
                <li>
                    <label @click="onTagClicked($event, 1)" :class="currentTab === 1 ? 'active' : ''">
                        <span class="bx bx-search"></span>
                        <span>Search Scores</span>
                    </label>
                </li>
                <li>
                    <label @click="onTagClicked($event, 2)" :class="currentTab === 2 ? 'active' : ''">
                        <span class="bx bx-file"></span>
                        <span>Reports</span>
                    </label>
                </li>
                <li>
                    <label>
                        <span class="bx bx-cog"></span>
                        <span>Settings</span>
                    </label>
                </li>
            </ul>
        </div>
        <main>
            <div class="card-container">
                <router-view></router-view>
            </div>
        </main>
    </div>
</template>

<style scoped>
.topbar {
    position: fixed;
    top: 0;
    left: 0;
    height: var(--topbar-h);
    width: 100%;
    background: #fff;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: left;
    font-size: 1.5rem;
}

.topbar-title h2 {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-left: 2rem;
    color: var(--main-color);
}

.topbar-title h4 {
    position: fixed;
    left: var(--sidebar-w);
    top: 0;
    width: 100%;
    height: var(--topbar-h);
    padding: 2rem 0 0 2.2rem;
    font-size: 1.2rem;
}

.sidebar {
    position: fixed;
    top: var(--topbar-h);
    left: 0;
    height: calc(100% - var(--topbar-h));
    width: var(--sidebar-w);
    z-index: 90;
}

.sidebar h4 {
    color: var(--main-color);
    margin: 1rem;
    padding: 2rem 0 1.2rem 1.2rem;
    font-size: 1.2rem;
    font-weight: 700;
}

.sidebar label {
    margin: 1rem 0 1rem 1rem;
    padding: 1.2rem 0 1.2rem 1.2rem;
    display: flex;
    color: var(--text-grey);
    align-items: center;
    border-radius: 2rem 0 0 2rem;
}

.sidebar label:hover {
    background: var(--background-color);
}

.sidebar .active {
    background: var(--main-color);
    color: white;
}

.sidebar .active:hover {
    background: var(--main-color);
    color: white;
}

.sidebar label span:first-child {
    font-size: 1.5rem;
    padding-right: 1rem;
}

.sidebar label span:last-child {
    font-size: 1.2rem;
}

main {
    margin-top: var(--topbar-h);
    margin-left: var(--sidebar-w);
    padding: 0 2rem 2rem 2rem;
    min-height: calc(100vh - var(--topbar-h));
    background: var(--background-color);
}

.card-container {
    display: flex;
    flex-direction: column;
}
</style>

<script>
export default {
    name: 'App',
    data() {
        return {
            currentTab: 1,
        }
    },
    mounted() {
        let path = String(window.location.href);
        this.currentTab = 1
        if (path.includes('/dashboard')) {
            this.currentTab = 0
        }
        else if (path.includes('/report')) {
            this.currentTab = 2
        }
    },
    methods: {
        checkRoute() {
            console.log(this.$route.path);
        },
        onTagClicked(e, tabId) {
            let tabNum = parseInt(tabId);
            if (tabNum === this.currentTab) {
                return;
            }
            switch (tabNum) {
                case 0:
                    this.currentTab = tabNum;
                    this.$router.push('/dashboard')
                    break;
                case 1:
                    this.currentTab = tabNum;
                    this.$router.push('/search')
                    break;
                case 2:
                    this.currentTab = tabNum;
                    this.$router.push('/report')
                    break;
                case 3:
                    this.currentTab = tabNum;
                    this.$router.push('/')
                    break;
            }
        }
    }
}
</script>