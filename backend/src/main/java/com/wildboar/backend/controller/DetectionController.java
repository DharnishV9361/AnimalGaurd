package com.wildboar.backend.controller;

import com.wildboar.backend.model.Detection;
import com.wildboar.backend.repository.DetectionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/api/detections")
public class DetectionController {

    @Autowired
    private DetectionRepository repository;

    @PostMapping
    public Detection createDetection(@RequestBody Detection detection) {
        detection.setTimestamp(LocalDateTime.now());
        return repository.save(detection);
    }

    @GetMapping
    public List<Detection> getAllDetections() {
        return repository.findAll();
    }
}
