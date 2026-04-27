package com.registry.verg.livestock.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.registry.verg.core.dto.CustomResponse;
import com.registry.verg.core.elasticsearch.dto.SearchCriteria;


public interface LiveStockService {

    CustomResponse createLiveStock(JsonNode liveStockEntity);

    CustomResponse  searchLiveStock(SearchCriteria searchCriteria);

    CustomResponse assignLiveStock(JsonNode liveStockEntity, String token);

    CustomResponse read(String id);

    CustomResponse delete(String id);
}