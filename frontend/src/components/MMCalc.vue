<template>
    <div class="tab-window">
        <h3>Moment Magnitude Calculator</h3>
        <hr />
        <b-input-group prepend="Length" append="km">
            <b-form-input v-model="mm_length" placeholder="249"></b-form-input>
        </b-input-group>
        <b-input-group prepend="Width" append="km">
            <b-form-input v-model="mm_width" placeholder="120.0"></b-form-input>
        </b-input-group>
        <b-input-group prepend="Slip" append="m">
            <b-form-input v-model="mm_slip" placeholder="23"></b-form-input>
        </b-input-group>
        <b-input-group prepend="Shear Modulus" append="10^11 dyne/cm^2">
            <b-form-input v-model="mm_shear" placeholder="3"></b-form-input>
        </b-input-group>
        <br />
        <b-button v-on:click="runMMC()" variant="success">Calculate</b-button>
        <br />
        <div v-show="SM != null && MM != null">
            <br />
            <hr />
            <h6><strong> Seismic Moment: </strong> {{this.SM}}</h6>
            <h6><strong> Moment Magnitude: </strong> {{this.MM}}</h6>
        </div>
    </div>
</template>

<script>
import { mapFields } from 'vuex-map-fields';

    export default {
        name: "MMCalc",
        data(){
            return {

            };
        },
      computed: {
        // mm_length: 249,
        // mm_width: 120.0,
        // mm_slip: 23,
        // mm_shear: 3,
        // SM: null,
        // MM: null,
        ...mapFields(['mmcalc.mm_length', 'mmcalc.mm_width', 'mmcalc.mm_slip', 'mmcalc.mm_shear', 'mmcalc.SM', 'mmcalc.MM'])
      },
        methods: {
            runMMC(){
                this.SM = (this.mm_length * this.mm_width * this.mm_slip * this.mm_shear * 1e23).toExponential(1);
                this.MM = (2 / 3 * Math.log(this.SM) / Math.log(10) - 10.7).toFixed(1);
            }
        }
    }
</script>

<style scoped>
    h6 {

    }
</style>