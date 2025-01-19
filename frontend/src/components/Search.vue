<template>
    <div class="search-page">
        <div class="container request">
            <h2 class="title">User Registration</h2>
            <div class="search-container">
                <input v-model="keyword" v-on:keyup.enter="onSearch" type="text"
                    placeholder="Enter registration number" />
                <button @click="onSearch" id="btn-search">Submit</button>
            </div>
        </div>
        <div class="container response">
            <h2 class="title">
                <span>Registration Number:</span>
                <span>{{ sbd }}</span>
            </h2>
            <div class="score-table">
                <table v-show="isExist">
                    <thead>
                        <tr>
                            <th style="width: 70%;">Subject</th>
                            <th style="width: 30%;">Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in subjectsShow">
                            <td>{{ item.view }}</td>
                            <td>{{ item.score }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </div>
</template>

<script>
import { fetchData } from '@/utils/api';

export default {
    name: 'Search',
    data() {
        return {
            keyword: "",
            scoreData: null,
            sbd: "<None>",
            subjectsShow: null,
            subjects: ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"],
            subjectMap: {
                "toan": "Mathematics",
                "ngu_van": "Literature",
                "ngoai_ngu": "Foreign Language",
                "vat_li": "Physics",
                "hoa_hoc": "Chemistry",
                "sinh_hoc": "Biology",
                "lich_su": "History",
                "dia_li": "Geography",
                "gdcd": "Civic Education"
            },
            isExist: false
        };
    },
    methods: {
        async onSearch() {
            try {
                let response = await fetchData(`check-score/${this.keyword}/`);
                if (response.status == 'success') {
                    this.scoreData = response.data;
                    this.sbd = this.scoreData.sbd;
                    this.subjectsShow = {};
                    for (const subject of this.subjects) {
                        if (this.scoreData[subject]) { 
                            this.subjectsShow[subject] = { 
                                "view": this.subjectMap[subject], 
                                "score": this.scoreData[subject] 
                            } 
                        };
                    };
                    this.isExist = true;
                } else if (response.status == 'not exist') {
                    this.sbd = this.keyword + ' does not exist!';
                    this.isExist = false;
                } else {
                    this.isExist = false;
                    throw new Error(response.message);
                }
            } catch (err) {
                console.log(err.message);
            }
        },
    },
};
</script>

<style scoped>
.container {
    width: 100%;
    margin-top: 2rem;
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);
    border-radius: 0.5rem;
    background: #fff;
    padding: 1rem;
}

.title {
    text-align: center;
    color: var(--main-color);
    margin-bottom: 1rem;
}

.search-container {
    display: flex;
    gap: 1rem;
    justify-content: center;
    max-width: 100%;
}

input {
    padding: 12px 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    width: 100%;
    max-width: 30%;
    font-size: 16px;
}

button {
    padding: 12px 25px;
    background-color: var(--main-color);
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    white-space: nowrap;
}

button:hover {
    background-color: var(--hover-color);
}

.response h2 span:first-child {
    color: #000;
    font-weight: 300;
    margin-right: 1rem;
}

.score-table {
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;
}

table {
    border-collapse: collapse;
    width: 20rem;
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

thead {
    background-color: var(--main-color);
    color: #fff;
}

th,
td {
    text-align: left;
    padding: 1rem 0 1rem 1.2rem;
}

tbody th {
    font-size: 1rem;
}

tbody tr:nth-child(odd) {
    background-color: #f9f9f9;
}

tbody tr:nth-child(even) {
    background-color: var(--background-color);
}

tbody tr:hover {
    background-color: #e2edff;
}
</style>