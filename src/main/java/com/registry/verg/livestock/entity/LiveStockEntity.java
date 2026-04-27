package com.registry.verg.livestock.entity;

import com.fasterxml.jackson.databind.JsonNode;

import java.sql.Timestamp;

import io.hypersistence.utils.hibernate.type.json.JsonBinaryType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.hibernate.annotations.Type;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "liveStock")
@Entity
public class LiveStockEntity {
    @Id
    private String liveStockId;

    @Type(JsonBinaryType.class)  // ✅ New Hibernate 6 syntax
    @Column(columnDefinition = "jsonb")
    private JsonNode data;

    private Timestamp createdOn;

    private Timestamp updatedOn;

    private String status;
}