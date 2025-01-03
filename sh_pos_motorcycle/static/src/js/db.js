/** @odoo-module */

import { PosDB } from "@point_of_sale/app/store/db";
import { patch } from "@web/core/utils/patch";


patch(PosDB.prototype, {
    setup() {
        super.setup();       
        this.motorcycle_type = [];
        this.motorcycle_make = [];
        this.motorcycle_model = [];
        this.all_motorcycle = [];
        this.motorcycle_year = [];
        this.produt_search_string = {};
        this.motorcycle_model_by_id = {};
        this.motorcycle_make_by_id = {};
        this.motorcycle_year_by_id = {};
    },
    get_motorcycle_type: function () {
        return this.motorcycle_type
    },
    get_motorcycle_make: function () {
        return this.motorcycle_make
    },
    get_motorcycle_by_id(id){
        var all = this.all_motorcycle;
        var result = {}
        for (const each of all) {
            if(each.id == id)
            {
                result = each
            }
        }
        return result
    },
    get_make_by_type(name) {
        var all = this.motorcycle_model
        var results = [];
        for (const each of all) {
            if (each.type_id[1] == name) {
                results.push(each)
            }
        }
        return results
    },
    get_model_by_make_and_type(make, type) {
        var all = this.motorcycle_model
        var results = []
        for (const each of all) {
            if (each.make_id[1] == make && each.type_id[1] == type) {
                results.push(each)
            }
        }
        return results
    },
    get_motorcycle_by_model(name) {
        var self = this;
        var all = this.all_motorcycle;
        var results = []
        for (const each of all) {
            if (each.mmodel_id && self.motorcycle_model_by_id[each.mmodel_id] && self.motorcycle_model_by_id[each.mmodel_id].display_name && self.motorcycle_model_by_id[each.mmodel_id].display_name == name) {
                results.push(each)
            }
        }
        return results
    },
    get_product_by_motorcycle(ids) {
        var products = []
        var self = this
        for (const id of ids) {
            products.push(self.get_product_by_id(id))
            
        }
        return products
    },
    search_product_in_motorcycle(category_id, query){
        try {
            query = query.replace(/[\[\]\(\)\+\*\?\.\-\!\&\^\$\|\~\_\{\}\:\,\\\/]/g,'.');
            query = query.replace(/ /g,'.+');
            var re = RegExp("([0-9]+):.*?"+utils.unaccent(query),"gi");
        }catch(e){
            return [];
        }
        var results = [];
        for(var i = 0; i < this.limit; i++){
            var r = re.exec(this.produt_search_string[category_id]);
            if(r){
                var id = Number(r[1]);
                results.push(this.get_product_by_id(id));
            }else{
                break;
            }
        }
        return results;
    }
})
