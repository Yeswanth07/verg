package com.registry.verg.seed.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.registry.verg.core.dto.CustomResponse;
import com.registry.verg.core.elasticsearch.dto.SearchCriteria;


public interface SeedService {

    CustomResponse createSeed(JsonNode seedEntity);

    CustomResponse searchSeed(SearchCriteria searchCriteria);

    CustomResponse assignSeed(JsonNode seedEntity, String token);

    CustomResponse read(String id);

    CustomResponse delete(String id);
}