package com.registry.verg.farmer.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.registry.verg.core.dto.CustomResponse;
import com.registry.verg.core.elasticsearch.dto.SearchCriteria;


public interface FarmerService {

    CustomResponse createFarmer(JsonNode farmerEntity);

    CustomResponse searchFarmer(SearchCriteria searchCriteria);

    CustomResponse assignFarmer(JsonNode farmerEntity, String token);

    CustomResponse read(String id);

    CustomResponse delete(String id);
}