package com.registry.verg.core.util;


public class Constants{

    public static final String ACTIVE = "ACTIVE";
    public static final String IN_ACTIVE = "INACTIVE";
    public static final String SUCCESSFULLY_CREATED = "successfully created";
    public static final String RESULT = "result";
    public static final String FAILED_CONST = "FAILED";
    public static final String ID = "id";

    public static final String ERROR = "ERROR";
    public static final String REDIS_KEY_PREFIX = "verg_cache_";


//ES Specific Constants
    public static final String INDEX_TYPE = "_doc";
    public static final String KEYWORD = ".keyword";
    public static final String ASC = "asc";
    public static final String MUST= "must";
    public static final String FILTER= "filter";
    public static final String MUST_NOT="must_not";
    public static final String SHOULD= "should";
    public static final String BOOL="bool";
    public static final String TERM="term";
    public static final String TERMS="terms";
    public static final String MATCH="match";
    public static final String RANGE="range";
    public static final String UNSUPPORTED_QUERY="Unsupported query type";
    public static final String UNSUPPORTED_RANGE= "Unsupported range condition";
    public static final String FACETS = "facets";
    public static final String COUNT = "count";
    public static final String SEARCH_OPERATION_LESS_THAN = "<";
    public static final String SEARCH_OPERATION_GREATER_THAN = ">";
    public static final String SEARCH_OPERATION_LESS_THAN_EQUALS = "<=";
    public static final String SEARCH_OPERATION_GREATER_THAN_EQUALS = ">=";




    private Constants() {
    }
}