package com.registry.verg.eagent.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.registry.verg.core.dto.CustomResponse;
import com.registry.verg.core.elasticsearch.dto.SearchCriteria;


public interface EagentService {

    CustomResponse createEagent(JsonNode eagentEntity);

    CustomResponse searchEagent(SearchCriteria searchCriteria);

    CustomResponse assignEagent(JsonNode eagentEntity, String token);

    CustomResponse read(String id);

    CustomResponse delete(String id);
}