<template>
    <div class="container">
        <h2 class="title">
            <span>Report</span>
        </h2>
        <div class="subject-select">
            <span class="subject-list-title">Subject:</span>
            <select name="class" v-model="subjectSelected" @change="updateSubject">
                <option v-for="subject in subjects" :value="subject.name" :key="subject.name">
                    {{ subject.view }}
                </option>
            </select>
        </div>

        <div id="chart">
            <BarChart :chartData="testData" :options="options" />
        </div>
    </div>
</template>

<script>
import { fetchData } from '@/utils/api';
import { BarChart } from 'vue-chart-3';
import { Chart, registerables } from "chart.js";
import { computed, ref } from 'vue';

Chart.register(...registerables);

export default {
    name: 'Report',
    components: { BarChart },

    setup() {
        const data = ref([30, 40, 60, 70]);

        const testData = computed(() => ({
            labels: ['<4', '≥4 && <6', '≥6 && <8', '≥ 8'],
            datasets: [
                {
                    label: 'Number of Students',
                    data: data.value,
                    backgroundColor: 'rgba(34, 87, 122, 0.7)',
                    borderRadius: 5
                },
            ],
        }));

        const options = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false // Hides the legend since it's unnecessary for this chart
                },
                tooltip: {
                    enabled: true // Displays tooltips when hovering
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
            categoryPercentage: 0.6,
        };

        function updateData() {
            data.value = this.scores;
        }

        return { testData, options, updateData };
    },
    data() {
        return {
            subjectSelected: 'toan',
            subjects: [
                { name: "toan", view: "Mathematics" },
                { name: "ngu_van", view: "Literature" },
                { name: "ngoai_ngu", view: "Foreign Language" },
                { name: "vat_li", view: "Physics" },
                { name: "hoa_hoc", view: "Chemistry" },
                { name: "sinh_hoc", view: "Biology" },
                { name: "lich_su", view: "History" },
                { name: "dia_li", view: "Geography" },
                { name: "gdcd", view: "Civic Education" }
            ],
            scores: [0,0,0,0],
            reports: null
        };
    },
    async mounted() {
        await this.getData();        
        this.updateSubject();
    },
    methods: {
        async getData() {
            try {
                let response = await fetchData('reports/');
                if (response.status == 'success') {
                    this.reports = response.data;
                    this.scores = this.reports.filter(item => item.subject === this.subjectSelected).map(item => item.student_count);
                } else {
                    throw new Error(response.message);
                }
            } catch (err) {
                console.log(err.message);
            }
        },
        updateSubject() {
            this.scores = this.reports.filter(item => item.subject === this.subjectSelected).map(item => item.student_count);
            this.updateData();
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
    margin-bottom: 2rem;
}

.subject-select {
    display: flex;
    align-items: center;
    justify-content: right;
    margin: 2rem 0;
}

.subject-list-title {
    padding: 0 10px;
    line-height: 15px;
    font-weight: 700;
}

select {
    height: 2.4rem;
    font-size: 1rem;
    margin-left: 10px;
    padding-left: 5px;
    border: 1px solid var(--text-color);
    border-radius: 5px;
    margin-right: 5rem;
}

#chart {
    text-align: center;
    max-width: 50rem;
    height: 60vh;
    margin: 0 auto;
}

</style>