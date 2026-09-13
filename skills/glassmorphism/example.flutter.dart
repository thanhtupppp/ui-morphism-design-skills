import 'dart:ui';
import 'package:flutter/material.dart';

class GlassSurface extends StatelessWidget {
  const GlassSurface({super.key, this.effectsEnabled = true, this.onPressed});

  final bool effectsEnabled;
  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        final padding = compact ? 12.0 : 16.0;
        final radius = compact ? 16.0 : 20.0;
        final surface = Container(
          padding: EdgeInsets.all(padding),
          decoration: BoxDecoration(
            color: effectsEnabled ? const Color(0x24FFFFFF) : Theme.of(context).colorScheme.surface,
            border: Border.all(color: effectsEnabled ? const Color(0x6BFFFFFF) : Theme.of(context).colorScheme.outline),
            borderRadius: BorderRadius.circular(radius),
          ),
          child: FilledButton(
            onPressed: onPressed,
            style: FilledButton.styleFrom(minimumSize: const Size(44, 44)),
            child: const Text('Open panel'),
          ),
        );

        if (!effectsEnabled) return surface;

        return ClipRRect(
          borderRadius: BorderRadius.circular(radius),
          child: BackdropFilter(
            filter: ImageFilter.blur(sigmaX: compact ? 14 : 20, sigmaY: compact ? 14 : 20),
            child: surface,
          ),
        );
      },
    );
  }
}
