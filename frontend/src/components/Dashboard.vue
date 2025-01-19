<template>
    <div class="container">
        <h2 class="title">Top 10 students of group A</h2>
        <div class="score-table">
            <table>
                <thead>
                    <tr>
                        <th style="width: 10%;">Top</th>
                        <th style="width: 25%;">Student ID</th>
                        <th style="width: 15%;">Total</th>
                        <th style="width: 10%;">Mth</th>
                        <th style="width: 10%;">Phy</th>
                        <th style="width: 10%;">Che</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(student, idx) in students">
                        <td>{{ idx + 1 }}</td>
                        <td>{{ student.sbd }}</td>
                        <td>{{ student.toan + student.vat_li + student.hoa_hoc }}</td>
                        <td>{{ student.toan }}</td>
                        <td>{{ student.vat_li }}</td>
                        <td>{{ student.hoa_hoc }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import { fetchData } from '@/utils/api';

export default {
    name: 'Dashboard',
    data() {
        return {
            students: null,
        };
    },
    async mounted() {
        try {
            let response = await fetchData('top-a00/');
            if (response.status == 'success') {
                this.students = response.data;
            } else {
                throw new Error(response.message);
            }
        } catch (err) {
            console.log(err.message);
        }
        
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

.score-table {
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;
}

table {
    border-collapse: collapse;
    width: 40rem;
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